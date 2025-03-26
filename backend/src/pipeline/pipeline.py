class Pipeline:
    def __init__(self):
        self.steps = []

    def run(self, data):
        for step in self.steps:
            data = step.process(data)
        return data

    def add_step(self, step):
        self.steps.append(step)