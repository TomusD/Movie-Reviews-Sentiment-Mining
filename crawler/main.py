import multiprocessing
import importlib

# Making each bot a new module to run in diffrent processes
def load_bot(bot_name):
    bot_module = importlib.import_module(bot_name)
    bot_module.loadBot()


if __name__ == "__main__":
    
    # Running the modules in different processes
    bot_names = ['PaginationBot1', 'PaginationBot2', 'PaginationBot3', 'PaginationBot4']

    for bot_name in bot_names:
        p = multiprocessing.Process(target=load_bot, args=(bot_name,))
        p.start()
