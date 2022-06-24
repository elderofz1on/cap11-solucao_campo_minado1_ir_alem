game.setScore(0)
game.setLife(3)
let jogador = game.createSprite(2, 2)
let bomba = game.createSprite(randint(0, 4), randint(0, 4))
let cronometro = 0
let velocidade = 450
basic.showString("GO!")
basic.forever(function () {
    basic.clearScreen()
    if (input.acceleration(Dimension.Y) < -40 && jogador.get(LedSpriteProperty.Y) > 0) {
        jogador.change(LedSpriteProperty.Y, -1)
    } else if (input.acceleration(Dimension.Y) > 40 && jogador.get(LedSpriteProperty.Y) < 4) {
        jogador.change(LedSpriteProperty.Y, 1)
    }
    if (input.acceleration(Dimension.X) < -40 && jogador.get(LedSpriteProperty.X) > 0) {
        jogador.change(LedSpriteProperty.X, -1)
    } else if (input.acceleration(Dimension.X) > 40 && jogador.get(LedSpriteProperty.X) < 4) {
        jogador.change(LedSpriteProperty.X, 1)
    }
    if (bomba.isTouching(jogador)) {
        game.addScore(1)
        bomba.set(LedSpriteProperty.X, randint(0, 4))
        bomba.set(LedSpriteProperty.Y, randint(0, 4))
        cronometro = 0
    }
    if (cronometro == 9) {
        basic.pause(100)
        game.removeLife(1)
        bomba.set(LedSpriteProperty.X, randint(0, 4))
        bomba.set(LedSpriteProperty.Y, randint(0, 4))
        cronometro = 0
    }
    cronometro += 1
    basic.pause(velocidade)
    if (velocidade > 250) {
        velocidade += -2
    }
    if (jogador.get(LedSpriteProperty.X) == 4) {
        jogador.set(LedSpriteProperty.X, 0)
    } else if (jogador.get(LedSpriteProperty.X) == 0) {
        jogador.set(LedSpriteProperty.X, 4)
    }
    if (jogador.get(LedSpriteProperty.Y) == 4) {
        jogador.set(LedSpriteProperty.Y, 0)
    } else if (jogador.get(LedSpriteProperty.Y) == 0) {
        jogador.set(LedSpriteProperty.Y, 4)
    }
})
