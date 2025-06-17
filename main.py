
def arithmetic_arranger(problems, show_answers=False):
    top_line = ""
    middle_line =""
    dash_line =""
    solution_line = ""


    #We check it the rules apply
    i = 0
    for equation in problems:
        i += 1
    if i > 5:
        return "Error: Too many problems."


    index = 0
    for equation in problems:
        parts = equation.split() #split into the three parts

        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if parts[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."


        #we also already and look which of the numbers is the longest
        longest = 0
        if len(parts[0]) > len(parts[2]):
            longest = len(parts[0]) +2

        elif len(parts[0]) < len(parts[2]):
            longest = len(parts[2]) +2
        else:
            longest = len(parts[0]) +2



        #we implement the formatting for the three lines
        if index == 0:
            top_line += parts[0].rjust(longest)
            middle_line += parts[1] + " " + parts[2].rjust(longest-2)
            dash_line += "-" * longest
            if show_answers:
                solution = str(eval(equation))
                solution_line += solution.rjust(longest)


            index += 1

        else:
            top_line += "    " + parts[0].rjust(longest)
            middle_line += "    " + parts[1] + " " +parts[2].rjust(longest-2)
            dash_line += "    " + "-" * longest
            if show_answers:
                solution = str(eval(equation))
                solution_line += "    " + solution.rjust(longest)



    if show_answers:
        SOLUTION = '\n'.join([top_line, middle_line, dash_line, solution_line])
    else:
        SOLUTION = '\n'.join([top_line, middle_line, dash_line])

    return SOLUTION



#test code of the instruction
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
