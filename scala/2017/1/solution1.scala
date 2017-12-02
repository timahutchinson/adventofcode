import scala.io.Source

var captcha = Source.fromFile("../../../python/2017/1/data.txt").getLines.mkString
captcha += captcha(0)
var total = 0

for (i <- Range(0,captcha.length-1)) {
  if (captcha(i) == captcha(i+1)) {
    total += captcha(i).asDigit
  }
}

println(f"Solution is $total")
