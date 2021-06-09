def custom_range(start, stop = None, step = None):
    if stop == None:
        stop = start + 0.0
        start = 0.0

    if step == None:
        step = 1.0

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break

        yield ("%g" % start)
        start += step

print("-" * 8 + "Custom range output" + "-" * 8)
for number in custom_range(10):
    print(number)

print("-" * 8 + "Custom range output" + "-" * 8)
for number in custom_range(1, 10):
    print(number)

print("-" * 8 + "Custom range output" + "-" * 8)
for number in custom_range(1, 10, 2):
    print(number)

print("-" * 12 + "Output end" + "-" * 12)
