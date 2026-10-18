document.getElementById("year").textContent=new Date().getFullYear();
const bus=document.querySelector(".moving-bus");const route=document.getElementById("route");
if(bus&&route&&!window.matchMedia("(prefers-reduced-motion: reduce)").matches){
const length=route.getTotalLength();let start;
function draw(t){if(!start)start=t;let n=((t-start)/28000)%1;const p=route.getPointAtLength(n*length),next=route.getPointAtLength(((n*length+2)%length));const angle=Math.atan2(next.y-p.y,next.x-p.x)*180/Math.PI;bus.setAttribute("transform",`translate(${p.x} ${p.y}) rotate(${angle})`);requestAnimationFrame(draw)}
requestAnimationFrame(draw);
}else if(bus){bus.setAttribute("transform","translate(180 118)")}
