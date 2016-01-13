# Двигайся к красной метке, избегая яков.
# используй Vector.normalize(vector1), чтобы создать вектор с тем же направлением, что и vector1, но c расстоянием 1 метр
# используй Vector.multiply(vector1, X), чтобы создать вектор с тем же направлением, что и vector1, но с расстоянием, умноженным на X

# Вот координаты красной метки.
goalPoint = Vector(78, 34)

loop:
    # Здесь создется вектор, который будет направлять героя на 10 метров в сторону goalPoint.
    # Для начала создай вектор от героя до красной метке.
    goal = Vector.subtract(goalPoint, self.pos)
    # Затем нормализуй его в вектор с расстоянием 1 метр.
    goal = Vector.normalize(goal)
    # И наконец, умножь вектор на 10, чтобы получить 10-ти метровый вектор.
    goal = Vector.multiply(goal, 10)
    
    # Чтобы обойти яка, когда он находится в пределах 10-ти метров, ты должен идти по вектору от него.
    yak = self.findNearest(self.findEnemies())
    distance = self.distanceTo(yak)
    if distance < 10:
        # Создай вектор от яка к герою.
        yak_vector = Vector.subtract(self.pos, yak.pos)
        # Теперь используй Vector.normalize и Vector.multiply, чтобы сделать этот вектор длиной 10 метров
        yak_vector = Vector.normalize(yak_vector)
        yak_vector = Vector.multiply(yak_vector, 10)
        # Если у тебя есть 10-метровый вектор от яка, используй Vector.add, чтобы добавить его к goal вектору!
        goal = Vector.add(yak_vector, goal)
        pass

    # И наконец, определи куда двигаться, добавив goal вектор к текущей позиции.
    moveToPos = Vector.add(self.pos, goal)
    self.move(moveToPos)
