# Personal Best (Bronze)

The supplied code is retained for audit, but it is **not a genuine synthesis
solution**: it mutates the grader's cost dictionary so expensive gates appear
free and then queues `QubitUnitary`. The regression test records this behavior
explicitly. A valid replacement must reduce circuit cost without changing the
cost model.
