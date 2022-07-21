import React from 'react';
import { usePagination, DOTS } from './usePagination';
const Pagination = props => {
    const {
        onPageChange,
        siblingCount = 1,
        currentPage,
        totalPageCount,
        nextPage,
        previousPage
    } = props;

    const paginationRange = usePagination({
        currentPage,
        siblingCount,
        totalPageCount,
        nextPage,
        previousPage
    });

    if (currentPage === 0 || paginationRange.length < 2) {
        return null;
    }

    const onNext = () => {
        onPageChange(currentPage + 1);
    };

    const onPrevious = () => {
        onPageChange(currentPage - 1);
    };

    let buttonClass;

    return (
        <div className="w3-center w3-padding-32">
            <div className="w3-bar">
                {(previousPage !== null && previousPage !== false) &&
                    <button className="w3-bar-item w3-button w3-hover-black" onClick={onPrevious}>«</button>
                }
                {paginationRange.map((pageNumber, index) => {
                    if (pageNumber === DOTS) {
                        return <span key={index} className="w3-bar-item">&#8230;</span>
                    }

                    if (currentPage === pageNumber) {
                        buttonClass = "w3-bar-item w3-button w3-black"
                    } else {
                        buttonClass = "w3-bar-item w3-button w3-hover-black"
                    }

                    return (
                        <button
                            key={index}
                            className={buttonClass}
                            onClick={() => onPageChange(pageNumber)}
                        >
                            {pageNumber}
                        </button>
                    );
                })}

                {(nextPage !== null && nextPage !== false) &&
                    <button className="w3-bar-item w3-button w3-hover-black" onClick={onNext}>»</button>
                }
            </div>
        </div>
    );
};

export default Pagination;