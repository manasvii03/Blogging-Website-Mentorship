import person from '../images/person.svg';
function Authorsyoulove(){
    return(
     <div className="authoursyoulove">
        <div className="authoursyouloveheadingdiv">
            <h3 className="authoursyouloveheading">Authors You Love</h3>
        </div>
        <div className="authorlayout">
         <button className="authorBtn"><div className="authorIcon"><img className="authorIconImg"src={person} alt="personIcon" height={35} width={35} /><p className="authorName">Kayla Writes</p></div></button>
         <button className="authorBtn"><div className="authorIcon"><img className="authorIconImg" src={person} alt="personIcon" height={35} width={35}/><p className="authorName">Aditi's Spot</p></div></button>
         <button className="authorBtn"><div className="authorIcon"><img className="authorIconImg" src={person} alt="personIcon" height={35} width={35}/><p className="authorName">Casual Reads</p></div></button>
     </div>
     </div>
    );
}
export default Authorsyoulove;