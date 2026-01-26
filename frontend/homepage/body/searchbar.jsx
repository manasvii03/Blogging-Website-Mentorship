import search from './images/Search.svg';
function searchbar(){
    return(
           <div className="searchWrapper">
             <img src={search} alt="search" className="searchIconInside" height={18} width={18}/>
             <input type="search" className="searchbar" placeholder="       Search For Your Next Favorite Blog"/>
           </div>
    );
}
export default searchbar;