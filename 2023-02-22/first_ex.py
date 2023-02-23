import logging

#logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def some_inputs(input_str: str, numb: int, fl_num: float) -> None:
    logging.info(f"Received tring {input_str}, number {numb} and float {fl_num}")
    if input_str == input_str[::-1]:
        logging.warning(f"Your string {input_str} is a palindrome!")
    try:
        numb = int(numb)
    except:
        logging.error(f"variable numb must be integer, now it is {type(numb)}")


some_inputs(input_str="Labas sabaL", numb="a", fl_num=5.2)