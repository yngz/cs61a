; Lab 13: Final Review - Optional Questions

; Q6
(define (nodots s)
        (define (dotted? s)
                (and (pair? s)
                     (not (or (pair? (cdr s)) (null? (cdr s))))
                )
        )
        (cond ((null? s) s)
              ((dotted? s) (list (nodots (car s)) (cdr s)))
              ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
              (else s)
        )
)

; Q7
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          (else (pair-tracker (cons curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
        (cond ((null? lst) #f)
              ((eq? (car lst) s) #t)
              (else (contains? (cdr lst) s))
        )
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)

; Q8
(define-macro (switch expr cases)
    'YOUR-CODE-HERE
)

