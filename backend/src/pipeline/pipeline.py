from pipeline.types.step_types import Step

class Pipeline:
    def __init__(self):
        self.step_instances = []

    def run(self, data):
        for step_instance in self.step_instances:
            data = step_instance.process(data)
        return data

    def add_step(self, step: Step):
        step_class = step.value
        step_instance = step_class()
        self.step_instances.append(step_instance)