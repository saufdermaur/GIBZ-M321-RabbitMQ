## Topic Exchange

### Emitter

```bash
python3 emit_topic.py
```

### Receivers

```bash
python3 receive_topic.py "error.#" "warning.cpu" "warning.memory"
```

```bash
python3 receive_topic.py "warning.#" "debug.#" "info.#"
```

```bash
python3 receive_topic.py "#"
```

### Inputs

```bash
error.network Network is down!
```
```bash
error.database Database connection lost!
```
```bash
warning.memory Memory usage is high!
```
```bash
warning.cpu CPU temperature is high!
```
```bash
warning.disk Disk space running low!
```
```bash
info.startup Application has started.
```
```bash
debug.auth User authentication successful.
```