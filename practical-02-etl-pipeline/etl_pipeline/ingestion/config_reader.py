def read_config(path="source_system/data/config.txt"):
    config = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
    return config

if __name__ == "__main__":
    print(read_config())