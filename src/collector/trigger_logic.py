import time


class TriggerAnalyzer:

    def __init__(self):

        # previous stable animal count
        self.previous_count = 0

        # periodic refresh timer
        self.last_periodic_trigger = 0

        # save semantic snapshot every 5 minutes
        self.periodic_interval = 300

        # anti-flicker logic
        self.zero_count_frames = 0

        # how many consecutive empty detections
        # before animals are considered gone
        self.zero_threshold = 10

        # anti-spam cooldown
        self.last_trigger_time = 0

        # minimum seconds between triggers
        self.min_trigger_gap = 30

    def should_trigger(self, current_count):

        now = time.time()

        # -----------------------------------
        # GLOBAL COOLDOWN
        # -----------------------------------

        if now - self.last_trigger_time < self.min_trigger_gap:
            return False

        # -----------------------------------
        # HANDLE TEMPORARY MISSED DETECTIONS
        # -----------------------------------

        if current_count == 0:

            self.zero_count_frames += 1

            # only reset state after
            # several consecutive empty frames
            if self.zero_count_frames >= self.zero_threshold:

                self.previous_count = 0

            return False

        # animal detected again
        self.zero_count_frames = 0

        # -----------------------------------
        # FIRST APPEARANCE
        # -----------------------------------

        if self.previous_count == 0:

            self.previous_count = current_count

            self.last_trigger_time = now

            return True

        # -----------------------------------
        # SIGNIFICANT COUNT CHANGE
        # -----------------------------------

        # avoids tiny YOLO fluctuations
        if abs(current_count - self.previous_count) >= 2:

            self.previous_count = current_count

            self.last_trigger_time = now

            return True

        # -----------------------------------
        # PERIODIC SNAPSHOT
        # -----------------------------------

        if now - self.last_periodic_trigger > self.periodic_interval:

            self.last_periodic_trigger = now

            self.last_trigger_time = now

            return True

        return False