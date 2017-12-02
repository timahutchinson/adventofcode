import scala.io.Source

var captcha = Source.fromFile("../../../data/2017/1/data.txt").getLines.mkString * 2
val n = captcha.length / 4
var total = 0

for (i <- Range(0,2*n)) {
  if (captcha(i) == captcha(i+n)) {
    total += captcha(i).asDigit
  }
}

println(f"Solution is $total")
