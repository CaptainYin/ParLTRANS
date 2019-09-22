program main

integer f(30)
do i=1,30
f(i)=1
enddo

do i=1,3
call update()
print*,'global f',f
enddo
contains

subroutine update()

use mpi

integer i,j,istr,iend,avgtask,extra
integer f(30)
integer, allocatable :: lf(:),kf(:)
integer code,np,world,ierr
character*8 name
!================================
!do i=1,30
!   do j=1,30
!     f(i,j)=i+j
!  enddo
!enddo

!do i=1,30
!   do j=1,30
!        g(i,j)=i*j
!          enddo
!          enddo

!============================

!single
!do i=1,3
! do j=1,3
 !  k(i,j)=f(i,j)+g(i,j)
 ! enddo
!enddo

!print*,k
!=============================


!parallel
call mpi_init(ierr)
call mpi_comm_dup(mpi_comm_world,world,ierr)
call mpi_comm_rank(world,code,ierr)
call mpi_comm_size(world,np,ierr)

status=hostnm(name)
!write(*,*)'i can',code
!write(*,*)'core number:',code,'from','  ',name


!lf=f(1:3,:)
!lg=g(1:3,:)
!lk=lf+lg
!print*,'fuck'
avgtask=30/np
extra=mod(30,np)
if(code .le. extra)then
        istr=(avgtask+1)*code+1
        iend=(avgtask+1)*(code+1)
else
        istr=avgtask*code+1+extra
        iend=avgtask*(code+1)+extra
endif
allocate(lf(iend-istr+1))
if(code.eq.0)then
allocate(kf(30))
endif

do i=1,iend-istr+1
lf(i)=10*code
enddo
call mpi_gather(lf,iend-istr+1,mpi_integer,kf,iend-istr+1,mpi_integer,0,world,ierr)

if(code.eq.0)then
print*,'code:',code,'kf:',kf
do i=1,30
f(i)=kf(i)
enddo
endif

deallocate(lf)

!print*,'Glowbal f',f
call mpi_comm_free(world,ierr)
call mpi_finalize(ierr)
end subroutine update

end program
