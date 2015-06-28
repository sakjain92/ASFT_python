#include "stp/c_interface.h"
#include <assert.h>

int main(int argc, char **argv) {
  VC vc = vc_createValidityChecker();

  // 32-bit variable 'c'
  Expr c = vc_varExpr(vc, "c", vc_bvType(vc, 32));

  // 32 bit constant value 5
  Expr a = vc_bvConstExprFromInt(vc, 32, 5);

  // 32 bit constant value 6
  Expr b = vc_bvConstExprFromInt(vc, 32, 6);

  // a+b!=c
  Expr xp1 = vc_bvPlusExpr(vc, 32, a, b);
  Expr eq = vc_eqExpr(vc, xp1, c);
  Expr eq2 = vc_notExpr(vc, eq);

  //Is a+b!=c always correct?
  int ret = vc_query(vc, eq2);

  //No, c=a+b is a counterexample
  assert(ret == 0);

  //print c = 11 counterexample
  vc_printCounterExample(vc);

  //Delete validity checker
  vc_Destroy(vc);

  return 0;
}
