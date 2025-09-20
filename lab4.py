processes = [
    {'id': 'P1', 'priority': 2, 'AT': 0, 'BT': 11},
    {'id': 'P2', 'priority': 0, 'AT': 5, 'BT': 28},
    {'id': 'P3', 'priority': 3, 'AT': 1, 'BT': 2},
    {'id': 'P4', 'priority': 1, 'AT': 2, 'BT': 10},
    {'id': 'P5', 'priority': 4, 'AT': 9, 'BT': 16},
]

processes.sort(key=lambda x: x['AT'])

n = len(processes)
completed = 0
current_time = 0
completed_processes = []

while completed < n:
   
    available = [p for p in processes if p['AT'] <= current_time and 'CT' not in p]
    if available:
        
        current_process = min(available, key=lambda x: x['priority'])
       
        current_process['CT'] = current_time + current_process['BT']
       
        current_process['TAT'] = current_process['CT'] - current_process['AT']
       
        current_process['WT'] = current_process['TAT'] - current_process['BT']
        
        current_time = current_process['CT']
        completed += 1
        completed_processes.append(current_process)
    else:
       
        current_time += 1


print(f"{'Process':<8}{'Priority':<10}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
for p in sorted(completed_processes, key=lambda x: x['id']):
    print(f"{p['id']:<8}{p['priority']:<10}{p['AT']:<5}{p['BT']:<5}{p['CT']:<5}{p['TAT']:<5}{p['WT']:<5}")
