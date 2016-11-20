#ifndef __PROJECT_EULER_LIB_H_
#define __PROJECT_EULER_LIB_H_

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

/* Macros so that we can use the calling function name (__func__) */
#define die() do {                                                    \
    fprintf(stderr, "%s failed\n", __func__);                         \
    exit(EXIT_FAILURE);                                               \
} while(0)

#define die_strerror() do {                                           \
    fprintf(stderr, "%s failed: %s\n", __func__, strerror(errno));    \
    exit(EXIT_FAILURE);                                               \
} while(0)


/* timespec_diff from: http://www.geonius.com/software/source/libgpl/ts_util.c */
int
_timespec_diff(
    struct timespec *res,
    struct timespec *begin,
    struct timespec *end)
{
    if ((end->tv_sec < begin->tv_sec) ||
        ((end->tv_sec == begin->tv_sec) &&
         (end->tv_nsec <= begin->tv_nsec))) {       /* TIME1 <= TIME2? */
        res->tv_sec = res->tv_nsec = 0 ;
    } else {                        /* TIME1 > TIME2 */
        res->tv_sec = end->tv_sec - begin->tv_sec ;
        if (end->tv_nsec < begin->tv_nsec) {
            res->tv_nsec = end->tv_nsec + 1000000000L - begin->tv_nsec ;
            res->tv_sec-- ;               /* Borrow a second. */
        } else {
            res->tv_nsec = end->tv_nsec - begin->tv_nsec ;
        }
    }
    return 0;
}

static void
_get_time(struct timespec *ts)
{
    /* monotonic to avoid jumps */
    if (clock_gettime(CLOCK_MONOTONIC, ts) != 0) {
        die_strerror();
    }
}

#define TIMED_RUN(expr) do {                                         \
    struct timespec ts_start, ts_end, ts_final;                      \
    _get_time(&ts_start);                                            \
    expr;                                                            \
    _get_time(&ts_end);                                              \
    _timespec_diff(&ts_final, &ts_start, &ts_end);                   \
    printf("%s: %ld.%.9lds\n",                                       \
            #expr,                                                   \
            ts_final.tv_sec,                                         \
            ts_final.tv_nsec);                                       \
} while (0)

#endif // __PROJECT_EULER_LIB_H_
