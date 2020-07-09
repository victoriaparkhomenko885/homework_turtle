# кирпичная стена
import turtle


def draw_consecutive_wall(lenght,high,wall):
    wall.right(90)
    wall.forward(high)
    wall.back(high)
    wall.left(90)
    wall.back(lenght)


def draw_square(side_square,high,witdh):
    wall = turtle.Turtle()
    wall.speed(10)
    counter_witdh= 0
    counter_high = 0
    Check_masonry = True # начало без полукирпичей 
    
    # проверка границ 
    wall.forward(side_square)
    wall.right(90)
    wall.forward(side_square)
    wall.right(90)
    wall.forward(side_square)
    wall.right(90)
    wall.forward(side_square)
    wall.right(90)
    wall.forward(side_square)
    

    while(True):
        if(side_square - high * counter_high > high):
            if(Check_masonry):  
          # последовательная стенка
                counter_witdh = 0
                while(True):
                    if(side_square - witdh * counter_witdh > witdh ):   
                        draw_consecutive_wall(witdh,high,wall) 
                        counter_witdh += 1                        
                    else:
                        draw_consecutive_wall(side_square - witdh * counter_witdh,high,wall)                        
                        break

                wall.right(90)
                wall.forward(high)
                wall.left(90)
                wall.forward(side_square)

                counter_high += 1
                Check_masonry = False


            else:
            # с полукирпича стенка
                counter_witdh = 0
                draw_consecutive_wall(witdh/2,high,wall)               

                while(True):
                    
                    if(side_square - (witdh * counter_witdh + witdh / 2) > witdh ):      
                        draw_consecutive_wall(witdh,high,wall)                       
                        counter_witdh += 1
                
                    else:
                        draw_consecutive_wall(side_square - (witdh * counter_witdh + witdh / 2),high,wall)                        
                        break

                wall.right(90)
                wall.forward(high)
                wall.left(90)
                wall.forward(side_square)

                counter_high += 1
                Check_masonry = True

        else:
            if(Check_masonry):  
            # последовательная стенка
                counter_witdh = 0
                while(True):
                    if side_square - witdh * counter_witdh > witdh :   
                        
                        draw_consecutive_wall(witdh,side_square - high * counter_high,wall)                        
                        counter_witdh += 1
                        
                    else:
                        draw_consecutive_wall(side_square - witdh * counter_witdh,side_square - high * counter_high,wall)                        
                        break

                wall.right(90)
                wall.forward(side_square - high * counter_high)
                wall.left(90)
                wall.forward(side_square)

                counter_high += 1
                Check_masonry = False


            else:
            # с полукирпича стенка
                counter_witdh = 0
                draw_consecutive_wall(witdh/2,side_square - high * counter_high,wall)
                while(True):
                    
                    if(side_square - (witdh * counter_witdh + witdh / 2) > witdh ):                    
                        draw_consecutive_wall(witdh,side_square - high * counter_high,wall)                        
                        counter_witdh += 1
                
                    else:
                        draw_consecutive_wall(side_square - (witdh * counter_witdh + witdh / 2),side_square - high * counter_high,wall)                        
                        break

                wall.right(90)
                wall.forward(side_square - high * counter_high)
                wall.left(90)
                wall.forward(side_square)

                counter_high += 1
                Check_masonry = True
                break    


draw_square(230,10,20)