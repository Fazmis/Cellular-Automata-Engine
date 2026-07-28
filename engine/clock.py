import time

class Clock:
    def __init__(self, fps=60):
        self.fps = 0
        self.target_frame_time = 0
        self.set_fps(fps)
        self.last_frame_time = time.perf_counter()

    def set_fps(self, fps) -> None:
        self.fps = fps
        if fps <= 0:
            self.target_frame_time = 0
        else:
            self.target_frame_time = 1 / fps

    def reset(self) -> None:
        self.last_frame_time = time.perf_counter()

    def tick(self) -> float:
        # before sleep
        execute_time = time.perf_counter() - self.last_frame_time
        time_to_sleep = max(0.0, self.target_frame_time - execute_time)
        time.sleep(time_to_sleep)
        # after sleep
        current_time = time.perf_counter()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return delta_time
