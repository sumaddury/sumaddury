def make_table ( data_sequence, num_o_columns ):
    table_str = ""
    for idx, ea_item in enumerate(data_sequence):
        table_str += str(ea_item) + "\t"
        if (idx+1) % num_o_columns == 0:
            table_str += "\n"
    """
    MODIFICATION:
    Since there can only be up to 1 return statement in a function, calling it inside the for loop, a loop which must iterate multiple times, will result in only the first iteration 
    being printed. As a result, the return statement must be moved to AFTER the for loop so that the entire calendar string will be returned.
    """
    return table_str

days = range(1,30)
week_days = 7
month_calendar = make_table(days, week_days)
print(month_calendar)