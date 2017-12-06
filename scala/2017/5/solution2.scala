import scala.io.Source
import scala.util.control.Breaks._

var vals = Source.fromFile("../../../data/2017/5/data.txt").getLines.toList.map(_.toInt)

var count: Int = 0
var ind: Int = 0
var old_val: Int = 0

while (true) {
  old_val = vals(ind)
  if (old_val >= 3) {
    vals = vals.updated(ind, old_val - 1)
  } else {
    vals = vals.updated(ind, old_val + 1)
  }
  count += 1
  ind += old_val
  if (ind >= vals.length) {
    println(f"Solution is $count")
    break
  }
}
