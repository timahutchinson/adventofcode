import scala.io.Source

val lines = Source.fromFile("../../../data/2017/2/data.txt").getLines.toList

var total = 0
for (line <- lines) {
  total += line.split("\\s").map(_.toInt).max - line.split("\\s").map(_.toInt).min
}

println(f"Solution is $total")
