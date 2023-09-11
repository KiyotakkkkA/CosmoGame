def check_collisions(object1, object2, y, is_bullet,  with_player=True):
    if not is_bullet:
        if (object2.x <= object1.x <= object2.x + object2.radius) or \
                (object2.x <= object1.x + object1.radius <= object2.x + object2.radius):

            if (object2.y <= y <= object2.y + object2.radius) or \
                (object2.y <= y + object1.radius <= object2.y + object2.radius):

                if not with_player:
                    object1.hp -= object2.damage
                return True
    else:
        if (object1.x < object2.x < object1.x + object1.radius) or \
                (object1.x < object2.x + object2.radius < object1.x + object2.radius):

            if (object2.y <= y <= object2.y + object2.radius) or \
                    (object2.y <= y + object1.radius <= object2.y + object2.radius):

                if not with_player:
                    object1.hp -= object2.damage
                return True