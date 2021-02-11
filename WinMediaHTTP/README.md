# Windows Multimedia HTTP Server
HTTP server for control multimedia on Windows.

### How To Use

Run script with double click or via `cmd`:
```bash
$ python main.py
```

> Open `http://localhost:8000/[endpoint]` in your browser

##### Endpoints
- `/play_pause` Play/Pause
- `/track_next` Next Track
- `/track_prev` Previous Track
- `/volume_up/[steps/default:2]` Volume UP
- `/volume_down/[steps/default:2]` Volume DOWN