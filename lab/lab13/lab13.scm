; Lab 13: Final Review

; Q3
(define (compose-all funcs)
		(define (helper funcs arg)
				(if (null? funcs) 
					arg
					(helper (cdr funcs)
							((car funcs) arg)
					)
				)
		)
  		(lambda (x) (helper funcs x))
)