import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from modules.parser import parser_auth_log
from modules.time_spike import detect_time_spikes

events = parser_auth_log("logs/auth.log")
spikes = detect_time_spikes(events)

for spike in spikes:
    print(spike)
