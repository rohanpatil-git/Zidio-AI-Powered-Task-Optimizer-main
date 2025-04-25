`task_recommender.py`
This module will recommend tasks based on the detected mood.
class TaskRecommender:
    def recommend_task(self, mood):
        tasks = {
            'happy': 'Work on creative projects',
            'neutral': 'Complete routine tasks',
            'stressed': 'Take a break or work on light tasks'
        }
        return tasks.get(mood, 'No recommendation available')
