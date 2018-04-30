subroutine fortran_kernel(n,x,y,z,tau,out)
    implicit none

    integer, parameter                    :: dp=kind(0.d0)
    integer,                 intent(in)   :: n
    real(dp), dimension(n),  intent(in)   :: x, y, z, tau
    real(dp), dimension(n),  intent(out)  :: out
    integer                               :: i, j
    real(dp)                              :: scale, d

    scale = 0.25_dp/(4.0_dp*atan(1.0_dp))

    out(:) = 0.0_dp
    do i = 1, n
        do j = 1, n
            if (i .ne. j) then
                d = sqrt((x(i)-x(j))**2 + (y(i)-y(j))**2 + (z(i)-z(j))**2)
                out(i) = out(i) + out(j)/d
            end if
        end do
    end do
    out(:) = out(:) * scale

end subroutine fortran_kernel

! f2py -m fortran_kernel -c kernel.f90
