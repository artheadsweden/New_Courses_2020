# Running this module will execute both print-statements
# But if we import this module, only the first one will run

print('I am outside the if-statement. The built in variable __name__ now equals', __name__)

if __name__ == '__main__':
    print('I am inside the if-statement')
