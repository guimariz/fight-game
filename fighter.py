import pygame

class Fighter():
  def __init__(self, x, y):
    self.rect = pygame.Rect((x, y, 80, 180))
    self.velocity_y = 0
    self.jump = False
    self.attack_type = 0

  def move(self, screen_width, screen_height, surface, target):
    SPEED = 10
    GRAVITY = 2
    delta_x = 0
    delta_y = 0

    # get keypresses
    key = pygame.key.get_pressed()

    # movement
    if key[pygame.K_a]:
      delta_x = -SPEED
    if key[pygame.K_d]:
      delta_x = SPEED      
    # jump
    if key[pygame.K_w] and self.jump == False:
      self.velocity_y = -30
      self.jump = True
    # attack
    if key[pygame.K_r] or key[pygame.K_t]:
      self.attack(surface, target)
      # determine with attack type was used
      if key[pygame.K_r]:
        self.attack_type = 1
      if key[pygame.K_t]:
        self.attack_type = 2

    # apply gravity
    self.velocity_y += GRAVITY
    delta_y += self.velocity_y

    # ensure player stays on screen
    if self.rect.left + delta_x < 0:
      delta_x = -self.rect.left
    if self.rect.right + delta_x > screen_width:
      delta_x = screen_width - self.rect.right
    if self.rect.bottom + delta_y > screen_height - 110:
      delta_y = 0
      self.jump = False
      delta_y = screen_height - 110 - self.rect.bottom

    # update player position
    self.rect.x += delta_x
    self.rect.y += delta_y

  def attack(self, surface, target):
    attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
    if attacking_rect.colliderect(target.rect):
      print('hit')

    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

  def draw(self, surface):
    pygame.draw.rect(surface, (255, 0, 0), self.rect)