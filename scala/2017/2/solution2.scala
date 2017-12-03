import scala.io.Source

val lines = Source.fromFile("../../../data/2017/2/data.txt").getLines.toList

var total = 0
for (line <- lines) {
  val split_line = line.split("\\s").map(_.toInt)
  val pairs = for (x <- split_line; y <- split_line) yield List(x,y)
  for (pair <- pairs) {
    if (pair(0) != pair(1)) {
      if (pair(0) % pair(1) == 0) {
        total += pair.max / pair.min
      }
    }
  }
}

println(f"Solution is $total")
