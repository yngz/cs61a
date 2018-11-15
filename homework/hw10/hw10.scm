(define (accumulate combiner start n term)
        (if (< n 1) start
            (combiner (term n) (accumulate combiner start (- n 1) term))
        )
)

(define (accumulate-tail combiner start n term)
        (if (< n 1) start
            (accumulate-tail combiner (combiner (term n) start) (- n 1) term)
        )
)

(define (partial-sums stream)
  'YOUR-CODE-HERE
  (helper 0 stream)
)

(define (rle s)
  'YOUR-CODE-HERE
)