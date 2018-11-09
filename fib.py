#!/usr/bin/env python3

# recursive fibonacci

def fib(last_term, current_term, current_count, count):
    '''Compute <count> fibonacci numbers recursively'''
    if current_count == count:
        return [current_term]
    else:
        return [current_term] + fib(current_term, last_term + current_term, current_count + 1, count)

def fib_helper(count):
    '''Return <count> fibonacci numbers'''
    if count == 0:
        return None
    else:
        fib_numbers = [0, 1]
        max_batch = 997
        if count > max_batch:
            fibs_left              = count
            (last_term, next_term) = fib_numbers[-2:]
            while fibs_left > 0:
                to_run                  = min(max_batch, fibs_left)
                fibs_left              -= to_run
                fib_numbers            += fib(next_term, last_term + next_term, 1, to_run)
                (last_term, next_term)  = fib_numbers[-2:]
        else:
            fib_numbers += fib(0, 1, 1, count)
        return fib_numbers

if __name__ == '__main__':
    from sys import argv, exit
    fibs = fib_helper(int(argv[1]))
    if len(argv) > 2:
        output_file = argv[2]
        with open(output_file, 'w') as f:
            for n in fibs:
                f.write(str(n) + "\n")
    else:
        print("\n".join([str(f) for f in fibs]))
    exit(0)
