import math


class ModelResult:

    def __init__(
        self,
        model_name: str,
        actuals: list,
        predictions: list,
        task: str = "classification",
    ):
        self.model_name = model_name
        self.actuals = actuals
        self.predictions = predictions
        self.task = task

        if len(actuals) != len(predictions):
            raise ValueError(
                f"actuals and predictions must be same length, "
                f"got {len(actuals)} and {len(predictions)}"
            )

    def accuracy(self) -> float:
        correct = sum(1 for a, p in zip(self.actuals, self.predictions) if a == p)
        return round(correct / len(self.actuals), 4)

    def rmse(self) -> float:

        return round(
            math.sqrt(
                sum(math.pow(a - p, 2) for a, p in zip(self.actuals, self.predictions))
                / len(self.actuals)
            ),
            4,
        )

    def f1_score(self) -> float:

        tp = sum(1 for a, p in zip(self.actuals, self.predictions) if a == 1 and p == 1)
        fp = sum(1 for a, p in zip(self.actuals, self.predictions) if a == 0 and p == 1)
        fn = sum(1 for a, p in zip(self.actuals, self.predictions) if a == 1 and p == 0)
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * (precision * recall) / (precision + recall)
        return round(f1, 4)

    def summary(self) -> dict:
        if self.task == "classification":
            return {
                "model": self.model_name,
                "task": self.task,
                "accuracy": self.accuracy(),
                "f1_score": self.f1_score(),
                "n_samples": len(self.actuals),
            }
        else:
            return {
                "model": self.model_name,
                "task": self.task,
                "rmse": self.rmse(),
                "n_samples": len(self.actuals),
            }

    def __repr__(self) -> str:
        return f"ModelResult(model={self.model_name!r}, task={self.task!r}, n={len(self.actuals)})"


# Test it
actuals = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
predictions = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]

result = ModelResult("random_forest", actuals, predictions)
print(result)

print(result.summary())

# Regression example
actuals_r = [10.0, 20.0, 30.0, 40.0, 50.0]
predictions_r = [11.0, 19.5, 31.0, 38.5, 52.0]

result_r = ModelResult("linear_regression", actuals_r, predictions_r, task="regression")
print(result_r.summary())
