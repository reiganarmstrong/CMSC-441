#include <gmpxx.h>

#include <chrono>
#include <iostream>
#include <queue>

using namespace std;
using namespace std::chrono;

// precondition: c = c % n
void step_function(mpz_t x, const mpz_t n, mpz_t c) {
    mpz_powm_ui(x, x, 2, n);
    mpz_add(x, x, c);
    mpz_mod(x, x, n);
}
// original and works
void pollard_rho(const mpz_t n, mpz_t ans, gmp_randstate_t rState,
                 bool &failed) {
    mpz_t i, x, y, c, k, d, y_m_x;
    mpz_inits(i, x, y, c, k, '\0');
    mpz_inits(d, y_m_x, '\0');
    mpz_set_ui(i, 1);
    mpz_set_ui(k, 2);
    mpz_urandomm(x, rState, n);
    mpz_set(y, x);
    mpz_urandomm(c, rState, n);
    mpz_mod(c, c, n);
    bool done = false;
    while (!done) {
        mpz_add_ui(i, i, 1);
        step_function(x, n, c);
        mpz_sub(y_m_x, y, x);
        mpz_abs(y_m_x, y_m_x);
        mpz_gcd(d, y_m_x, n);
        if (mpz_cmp_ui(d, 1) != 0) {
            if (mpz_cmp(d, n) == 0) {
                failed = true;
            } else {
                mpz_set(ans, d);
                failed = false;
            }
            done = true;
        } else {
            if (mpz_cmp(k, i) == 0) {
                mpz_set(y, x);
                mpz_mul_2exp(k, k, 1);
            }
        }
    }
}

void pollard_rho_modified(const mpz_t n, mpz_t ans, gmp_randstate_t rState,
                          bool &failed) {
    int zCounter = 1;
    mpz_t i, x, y, c, k, d, y_m_x, z;
    mpz_inits(i, x, y, c, k, '\0');
    mpz_inits(d, y_m_x, z, '\0');
    mpz_set_ui(i, 1);
    mpz_set_ui(z, 1);
    mpz_set_ui(k, 2);
    mpz_urandomm(x, rState, n);
    mpz_set(y, x);
    mpz_urandomm(c, rState, n);
    mpz_mod(c, c, n);
    bool done = false;
    int numSteps = 0;
    while (!done) {
        mpz_add_ui(i, i, 1);
        step_function(x, n, c);
        mpz_sub(y_m_x, y, x);
        mpz_abs(y_m_x, y_m_x);
        if (mpz_cmp_ui(k, 100) >= 0) {
            mpz_mul(z, z, y_m_x);
            zCounter++;
            if (zCounter == 100) {
                numSteps++;
                mpz_mod(z, z, n);
                mpz_gcd(d, z, n);
            }
        } else {
            mpz_gcd(d, y_m_x, n);
        }
        if (mpz_cmp_ui(d, 1) != 0) {
            if (mpz_cmp(d, n) == 0) {
                failed = true;
            } else {
                mpz_set(ans, d);
                failed = false;
            }
            done = true;
        } else {
            if (mpz_cmp(k, i) == 0) {
                mpz_set(y, x);
                mpz_mul_2exp(k, k, 1);
            }
        }
        if (zCounter == 100) {
            zCounter = 0;
            mpz_set_ui(z, 1);
        }
    }
}

void pollard_rho_multi_threading(const mpz_t n, mpz_t ans,
                                 gmp_randstate_t rState, bool &failed) {
    int zCounter = 1;
    mpz_t i, x, y, c, k, d, y_m_x, z;
    mpz_inits(i, x, y, c, k, '\0');
    mpz_inits(d, y_m_x, z, '\0');
    mpz_set_ui(i, 1);
    mpz_set_ui(z, 1);
    mpz_set_ui(k, 2);
    mpz_urandomm(x, rState, n);
    mpz_set(y, x);
    mpz_urandomm(c, rState, n);
    mpz_mod(c, c, n);
    bool done = false;
    int numSteps = 0;
    while (!done) {
        mpz_add_ui(i, i, 1);
        step_function(x, n, c);
        mpz_sub(y_m_x, y, x);
        mpz_abs(y_m_x, y_m_x);
        if (mpz_cmp_ui(k, 100) >= 0) {
            mpz_mul(z, z, y_m_x);
            zCounter++;
            if (zCounter == 100) {
                numSteps++;
                mpz_mod(z, z, n);
                mpz_gcd(d, z, n);
            }
        } else {
            mpz_gcd(d, y_m_x, n);
        }
        if (mpz_cmp_ui(d, 1) != 0) {
            if (mpz_cmp(d, n) == 0) {
                failed = true;
            } else {
                mpz_set(ans, d);
                failed = false;
            }
            done = true;
        } else {
            if (mpz_cmp(k, i) == 0) {
                mpz_set(y, x);
                mpz_mul_2exp(k, k, 1);
            }
        }
        if (zCounter == 100) {
            zCounter = 0;
            mpz_set_ui(z, 1);
        }
    }
}
int main(int argc, char const *argv[]) {
    bool failed;
    mpz_t a, b, c;
    mpz_inits(a, b, c, '\0');
    mpz_set_str(a, "45319868827794527371331674843886952588281", 0);
    cout << numbers << endl;
    gmp_randstate_t rState;
    gmp_randinit_mt(rState);
    gmp_randseed_ui(rState, time(0));
    pollard_rho_modified(a, c, rState, failed);
    cout << c << endl;
    mpz_div(b, a, c);
    cout << b << endl;
}
