import datetime

class Task:
    """calss for managing tasks"""
    def __init__(self,task_id,name,description="",status=False,
                 start_time=None,end_time=None):
        self.id=task_id
        self.name=name
        self.descrition=description
        self.status=status
        self.start_time=start_time
        self.end_time=end_time
    def mark_done(self):
        """mark the task as done"""
        self.status=True
    def set_time(self,start_time,end_time):
        """set the start and the end times and calculate the duration"""
        self.start_time=start_time
        self.end_time=end_time
    def get_duration(self):
        """calculate the duration of the task"""
        if self.start_time and self.end_time:
            duration=self.end_time - self.start_time
            return duration.total_seconds() / 3600
        return None
    def __str__(self):
        return(f'Task ID:{self.id},Name:{self.name},Description:{self.descrition},'
               f"Status:{'Done' if self.status else 'Not Done'},"
               f"Start Time:{self.start_time},End Time:{self.end_time},"
               f"Duration:{self.get_duration()} hours")
    