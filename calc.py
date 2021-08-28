import sys
import random
import time

solved_addition = {}
solved_subtraction = {}
timer_problem = {}
log_file = open("practice.log", "a")

def get_rand(operator, first=None):
  if operator == "+":
    return random.randrange(1, 11)

  if operator == "-":
    if first is None:
       return random.randrange(2, 21)
    else:
       return random.randrange(1, first)
  return None

def get_result(prompt, correct):
  start_time = time.time()
  while True:
    try:
      answer = int(raw_input(prompt + " = ? "))
    except ValueError:
      answer = -1
    if correct == answer:
      print "Yes!"
      answer_time = time.time() - start_time
      write_logs(prompt, answer_time)
      timer_problem[prompt] = answer_time
      return True

def subtraction_prob():
  while True:
    first_num = get_rand("-")
    second_num = get_rand("-", first_num)
    if not (first_num, second_num) in solved_subtraction:
        break
  solved_subtraction[(first_num, second_num)] = 1
  prompt = "%d - %d" % (first_num, second_num)
  get_result(prompt, first_num - second_num)


def addition_prob():
  while True:
    first_num = get_rand("+")
    second_num = get_rand("+")
    if not (first_num, second_num) in solved_addition:
        break
  solved_addition[(first_num, second_num)] = 1
  prompt = "%d + %d" % (first_num, second_num)
  get_result(prompt, first_num + second_num)

def write_logs(prompt, answer_time):
  log_file.write("%s : %d\n" % (prompt, answer_time))    

def show_stats():
  count = 0 
  for item in sorted(timer_problem.items(), key=lambda x: -x[1]):
     if item[1] < 3:
       break
     if count == 0:
       print "Problems to improve"
     print "%s: %d sec" % (item[0], item[1])
     count += 1
     if count >= 5:
        break

def main():
  total = 0
  total_prob = 100
  start_time = time.time()
  log_file.write("#Practiced on %s\n" % time.strftime("%Y-%m-%d %H:%M"))
  for i in range(0, total_prob):
     total += 1
     print "%d) " % total,
     if i < total_prob/2: 
        addition_prob()
     else:
        subtraction_prob()
  print "Total %d problems" % total
  end_time = time.time()
  total_time = end_time - start_time
  print "You total time spent = %d seconds, avg time = %.1f sec per problem" % (total_time, total_time*1.0/total)
  show_stats()

main()


