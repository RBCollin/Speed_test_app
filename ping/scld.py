import schedule
import time
import sched


### METODO DE UM EM UM SEGUNDO 

# scheduler = sched.scheduler()

# def func():
#     print('Olha ta rodando em carai')

# schedule.every(1).seconds.do(func)


# while True:
#     schedule.run_pending()
#     print('Running...')
#     time.sleep(1)


def my_job():
    print('Foo')

# Run every 5 to 10 seconds.
schedule.every(5).seconds.do(my_job)

while True:
    
    schedule.run_pending()



### METODO INFINITO

# import schedule
# import time
# import sched



# scheduler = sched.scheduler()

# def func():
#     print('Olha ta rodando em carai')

#     scheduler.enter(delay=1, priority=0, action=func)

# func()


# try:
#     scheduler.run(blocking=True)

# except KeyboardInterrupt:

#     print('Programa finalizado!')