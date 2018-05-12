# coding=utf-8
import sys
from Queue import Queue


def solve(machines, tasks):
    solutions = {
        "plan": {},
        "value": 0
    }
    if len(tasks) == 0:
        for machine in machines:
            solutions["plan"][machine] = None
        return solutions
    sub_tasks = []
    for i in range(0, len(tasks) - 1):
        sub_tasks.append(tasks[i])
    current_task = tasks[len(tasks) - 1]
    sub_solutions = solve(machines, sub_tasks)
    solutions = sub_solutions.copy()
    # 先找空位分配
    for machine in machines:
        if sub_solutions[machine] == None:
            if machine[0] >= current_task[0] and machine[1] >= current_task[1]:
                solutions["plan"][machine] = current_task
                solutions["value"] += 200 * current_task[0] + 3 * current_task[1]
                return solutions
            else:
                pass
        else:
            pass
    # 没有空位则交换
    for machine in machines:
        if machine[0] >= current_task[0] and machine[1] >= current_task[1]:
            new_value = 200 * current_task[0] + 3 * current_task[1]
            old_value = 200 * solutions["plan"][machine][0] + 3 * solutions["plan"][machine][1]
            if new_value > old_value:
                new_task = solutions["plan"][machine]
                solutions["plan"][machine] = current_task
                solutions["value"] += new_value - old_value
    return solutions


if __name__ == "__main__":
    ans = 0
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, m = map(int, line.split())
    machine_num = 0
    machines = []
    tasks = Queue()
    plans = {}
    for i in range(n):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        machine = map(int, line.split())
        machines.append(machine)
        plans[machine_num] = None
        machine_num += 1
    for i in range(m):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        tasks.put(map(int, line.split()))
    count = 0
    value = 0
    task_num = tasks.qsize()
    while tasks.qsize() > 0 and count < tasks.qsize():
        # 取出一个进行安置
        task = tasks.get()
        is_set = False
        # 遍历机器
        for machine_id in plans.keys():
            machine = machines[machine_id]
            if plans[machine_id] == None:
                if machine[0] >= task[0] and machine[1] >= task[1]:
                    plans[machine_id] = task
                    is_set = True
                    value += 200 * task[0] + 3 * task[1]
                    break
                else:
                    continue
            else:
                # 如果机床能力足够
                if machine[0] >= task[0] and machine[1] >= task[1]:
                    # 比较价值大小
                    old_value = 200 * plans[machine_id][0] + 3 * plans[machine_id][1]
                    new_value = 200 * task[0] + 3 * task[1]
                    if new_value > old_value:
                        # 有价值提升则换掉
                        tasks.put(plans[machine_id])
                        plans[machine_id] = task
                        value += new_value - old_value
                        is_set = True
                        break
                    else:
                        continue
        if not is_set:
            tasks.put(task)
            count += 1
        else:
            count=0
        print("Queue:")
        print(tasks.queue)
        print("plans:")
        print(plans)
    for machine_id in plans.keys():
        if plans[machine_id]:
            ans += 1
    print(plans)
    print ans, " ", value
