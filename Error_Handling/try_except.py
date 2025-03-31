for val in range(1, 6):
    try:
          if val==3:
                raise ValueError("Value is 3")
          else:
                print(val)   
    except ValueError as e:
          print(f"Error is : {e}")
          break
    finally:
          print(f"Finally block is executed on {val}")