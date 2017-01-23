def createGreeter = { name ->
  return {
    def day = 0
    if (day == 0 || day == 6) {
      println "Nice Weekend, $name"
    } else {
      println "Hello, $name"
    }
  }
}
def greetWorld = createGreeter("World")
greetWorld()
