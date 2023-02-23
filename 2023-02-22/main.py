import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def add_num(a: int, b :int) -> int:
    #logging.debug(f"received numbers: a {a} and b {b}")
    logging.warning(f"received numbers: a {a} and b {b}")
    return a + b

add_num(a=6, b=8)

#-------------------------------------------------------

def amount_money(amount: int) -> None:
    logging.info(f"Amount received: {amount}")
    if amount == 0:
        logging.warning("expected amount higher than zero")

#-------------------------------------------------------

try:
    2 + 2
except Exception as e:
    logging.error("Error received: {e}")

#-------------------------------------------------------

def emergency_stop(is_stop_event: bool) -> None:
    if is_stop_event:
        logging.critical(f"Had to stop due to emergency")
        #stopper function

#--------------------------------------------------------

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def add_num_two(a: int, b :int) -> int:
    #logging.debug(f"received numbers: a {a} and b {b}")
    logging.warning(f"received numbers: a {a} and b {b}")
    return a + b

add_num(a=6, b=8)