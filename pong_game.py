import pygame
import random
import sys

# Inizializzazione pygame
pygame.init()

# Colori
bianco = (255, 255, 255)
azzurro = (0, 189, 132)

# Suoni
pygame.mixer.init()
suono_palla = pygame.mixer.Sound('ping_pong_8bit_plop.ogg')

# Creazione finestra di gioco
larghezza_finestra = 800
altezza_finestra = 600

finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("Pong")

# Controllo degli FPS
clock = pygame.time.Clock()
fps = 60

# Creazione delle racchette
larghezza_racchetta = 15
altezza_racchetta = 100
velocita_racchetta = 5

racchetta_sinistra = pygame.Rect(50, altezza_finestra // 2 - altezza_racchetta // 2,
                                 larghezza_racchetta, altezza_racchetta)

racchetta_destra = pygame.Rect(larghezza_finestra - 50 - larghezza_racchetta,
                               altezza_finestra // 2 - altezza_racchetta // 2,
                               larghezza_racchetta, altezza_racchetta)

# Creazione della palla
dimensione_palla = 20
velocita_palla_x = 5
velocita_palla_y = 5

palla = pygame.Rect(larghezza_finestra // 2 - dimensione_palla // 2,
                    altezza_finestra // 2 - dimensione_palla // 2,
                    dimensione_palla,
                    dimensione_palla)

# Punteggio
punteggio_sinistra = 0
punteggio_destra = 0
font = pygame.font.SysFont("Arial", 60, bold=True, italic=False)

# Giocatore che ha colpito la palla per ultimo
ultimo_giocatore = None

# Funzione per disegnare gli oggetti sullo schermo
def disegna_oggetti():
    finestra.fill(azzurro)
    pygame.draw.rect(finestra, bianco, racchetta_sinistra)
    pygame.draw.rect(finestra, bianco, racchetta_destra)
    pygame.draw.ellipse(finestra, bianco, palla)

    testo_sinistra = font.render(str(punteggio_sinistra), True, bianco)
    testo_destra = font.render(str(punteggio_destra), True, bianco)
    finestra.blit(testo_sinistra, (larghezza_finestra // 4 - testo_sinistra.get_width() // 2, 20))
    finestra.blit(testo_destra, (3 * larghezza_finestra // 4 - testo_destra.get_width() // 2, 20))

def onboarding():
    # Funzione per ottenere i nomi dei giocatori
    def get_player_name(player_num):
        pygame.display.set_caption(f"Inserisci il nome del giocatore {player_num}")
        input_box = pygame.Rect(300, 250, 200, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        font = pygame.font.Font(None, 32)
        done = False
        
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            finestra.fill((30, 30, 30))
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            finestra.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(finestra, color, input_box, 2)
            pygame.display.flip()
            clock.tick(30)
        return text
    
    giocatore1 = get_player_name(1)
    giocatore2 = get_player_name(2)
    return giocatore1, giocatore2

# Avvio dell'onboarding
giocatore1, giocatore2 = onboarding()

# Ciclo infinito
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento delle racchette
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_w] and racchetta_sinistra.top > 0:
        racchetta_sinistra.y -= velocita_racchetta
    if tasti[pygame.K_s] and racchetta_sinistra.bottom < altezza_finestra:
        racchetta_sinistra.y += velocita_racchetta
    if tasti[pygame.K_UP] and racchetta_destra.top > 0:
        racchetta_destra.y -= velocita_racchetta
    if tasti[pygame.K_DOWN] and racchetta_destra.bottom < altezza_finestra:
        racchetta_destra.y += velocita_racchetta

    # Movimento della palla
    palla.x += velocita_palla_x
    palla.y += velocita_palla_y

    # La palla collide con i bordi verticali
    if palla.top <= 0 or palla.bottom >= altezza_finestra:
        velocita_palla_y = -velocita_palla_y
        suono_palla.play()

    # La palla collide con i bordi orizzontali
    if palla.left <= 0 or palla.right >= larghezza_finestra:
        if palla.left <= 0 and ultimo_giocatore == "destra":
            punteggio_destra += 1
        elif palla.right >= larghezza_finestra and ultimo_giocatore == "sinistra":
            punteggio_sinistra += 1

        palla.x = larghezza_finestra // 2 - dimensione_palla // 2
        palla.y = altezza_finestra // 2 - dimensione_palla // 2
        velocita_palla_x = random.choice([-5, 5])
        velocita_palla_y = random.choice([-5, 5])

        ultimo_giocatore = None

    # La palla collide con le racchette
    if palla.colliderect(racchetta_sinistra):
        velocita_palla_x = -velocita_palla_x
        ultimo_giocatore = "sinistra"
        suono_palla.play()
    elif palla.colliderect(racchetta_destra):
        velocita_palla_x = -velocita_palla_x
        ultimo_giocatore = "destra"
        suono_palla.play()

    disegna_oggetti()

    pygame.display.update()
    clock.tick(fps)

