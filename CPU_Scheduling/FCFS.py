# FCFS scheduling

# total wait time
def getWaitingTime(processes, n, bt, wt):
	wt[0] = 0
	for i in range(1, n):
		wt[i] = bt[i - 1] + wt[i - 1]

# total turn around time
def getTurnAroundTime(processes, n, bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt):
  wt = [0] * n
  tat = [0] * n
  total_wt = 0
  total_tat = 0

  getWaitingTime(processes, n, bt, wt)
  getTurnAroundTime(processes, n, bt, wt, tat)


  # Output
  print( "Processes | Burst time | Waiting time | Turn around time | Reponse time")

  for i in range(n):
    total_wt = total_wt + wt[i]
    total_tat = total_tat + tat[i]

    print(" " + str(i + 1) + "\t\t" +
      str(bt[i]) + "\t\t" +
      str(wt[i]) + "\t\t" +
      str(tat[i]) + "\t\t" +
      str(tat[i]))

  print("\nAvg Wait time = " + str(total_wt / n))
  print("Avg Turn Around time = " + str(total_tat / n))
  print("Avg Response time = " + str(total_tat / n))
  print("\n")

# Main method
if __name__ =="__main__":
	processes = [1, 2, 3]
	n = len(processes)
	burst_time = [10, 5, 8]

	findavgTime(processes, n, burst_time)

