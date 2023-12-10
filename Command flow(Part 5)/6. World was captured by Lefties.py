message = ("left", "right", "left", "stop", "bright aright", "ok", "enough", "jokes")
result = ",".join(message)
result = result.replace("right", "left")
print(result)
