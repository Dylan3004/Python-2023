import pygame, sys , random
pygame.init()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.image = pygame.image.load('enemy.jpg')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect(center=(x, y))
        self.screen = screen

    def update(self):
        self.screen.blit(self.image, self.rect)




def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption('Cyber Ball')
    icon = pygame.image.load('ikona.jpg')
    pygame.display.set_icon(icon)
    pygame.mixer.music.load(r'audio.mp3')
    pygame.mixer.music.play(-1)
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    speed = [0, 0]
    accel = [0.1, 0.1]
    image = pygame.image.load(r'tlo.jpg')


    image = pygame.transform.scale(image, size)
    surf_center = (
    (width - image.get_width()) / 2,
    (height - image.get_height()) / 2
    )
    screen.blit(image, surf_center)
    ball = pygame.image.load('ball.gif')
    ball = pygame.transform.scale(ball, (ball.get_width() // 5, ball.get_height() // 5))
    screen.blit(ball, (width / 2, height / 2))
    ballrect = ball.get_rect(center=(width / 2, height / 2))
    pygame.display.flip()

    enemies = pygame.sprite.Group()
    for _ in range(10):  # Creating 10 enemies at random positions
        enemy = Enemy(screen, random.randint(0, width), random.randint(0, height))
        enemies.add(enemy)

    font = pygame.font.Font(None, 36)
    score = 0
    newscore = False
    velocity = 1
    velocitytable = [1,1,1,1] # up , down , left , right

    while True:
        i = 0
        if i == 0:
            for enemy in enemies:
                screen.blit(enemy.image, enemy.rect)  # Draw each enemy
                score_text = font.render(f'Score: {score}', True, (255, 255, 255))
                screen.blit(score_text, (40, 40))
            pygame.display.flip()
        i = 1
        if score == 50:
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'YOU WON', True, (255, 0, 0))
            screen.blit(score_text, (width/2-50, height/2))
            pygame.display.flip()
            pygame.time.delay(5000)
            sys.exit()

        clock.tick(60)
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: sys.exit()
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            # zamienić na jakieś przeliczenie
            speed[1]-=0.1 *velocitytable[0]
            speed[0]-=0.1 *velocitytable[2]
            velocitytable[0] += 0.2
            velocitytable[2] += 0.2
            velocitytable[1] = 1
            velocitytable[3] = 1
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            speed[1]-=0.1 *velocitytable[0]
            speed[0]+=0.1 *velocitytable[3]
            velocitytable[0] += 0.2
            velocitytable[3] += 0.2
            velocitytable[1] = 1
            velocitytable[2] = 1
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            speed[1]+=0.1 *velocitytable[1]
            speed[0]-=0.1 *velocitytable[2]
            velocitytable[1] += 0.2
            velocitytable[2] += 0.2
            velocitytable[0] = 1
            velocitytable[3] = 1
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            speed[1]+=0.1 *velocitytable[1]
            speed[0]+=0.1 *velocitytable[3]
            velocitytable[1] += 0.2
            velocitytable[3] += 0.2
            velocitytable[0] = 1
            velocitytable[2] = 1

        elif keys[pygame.K_UP]:
            speed[1]-=0.1 *velocitytable[0]
            velocitytable[0] += 0.2
            velocitytable[1] = 1
            velocitytable[2] = 1
            velocitytable[3] = 1
        elif keys[pygame.K_DOWN]:
            speed[1]+=0.1 *velocitytable[1]
            velocitytable[1] += 0.2
            velocitytable[0] = 1
            velocitytable[2] = 1
            velocitytable[3] = 1
        elif keys[pygame.K_LEFT]:
            speed[0]-=0.1 *velocitytable[2]
            velocitytable[2] += 0.2
            velocitytable[0] = 1
            velocitytable[1] = 1
            velocitytable[3] = 1
        elif keys[pygame.K_RIGHT]:
            speed[0]+=0.1 *velocitytable[3]
            velocitytable[3] += 0.2
            velocitytable[0] = 1
            velocitytable[1] = 1
            velocitytable[2] = 1
        ballrect = ballrect.move(speed)

        for enemy in enemies:
            if ballrect.colliderect(enemy.rect):  # Check collision
                enemies.remove(enemy)
                if score < 40:
                    enemy = Enemy(screen, random.randint(0, width), random.randint(0, height))
                    enemies.add(enemy)
                score += 1
                score_text = font.render(f'Score: {score}', True, (255, 255, 255))
                screen.blit(score_text, (40, 40))

                screen.blit(ball, ballrect)
                for enemy in enemies:
                    screen.blit(enemy.image, enemy.rect)  # Draw each enemy
                pygame.display.flip()

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
