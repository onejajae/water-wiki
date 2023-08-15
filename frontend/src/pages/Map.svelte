<script>
    import MapSupplierList from "../components/Map/MapSupplierList.svelte";
    import { supplierApi } from "../api";
    import { onMount } from "svelte";
    import MarkerClustering from "../utils/marker-tools/js/MarkerClustering";

    let suppliers = []
    let selectedSupplier;
    let map;
    
    const mapOptions = {
        center: new naver.maps.LatLng(36.2253017, 127.6460516),
        zoom: 7,
        zoomControl: true,
        zoomControlOptions: {
            position: naver.maps.Position.TOP_LEFT,
            style: naver.maps.ZoomControlStyle.SMALL,
        },
        logoControl: false,
        mapDataControl: false,
        scaleControl: false
    }

    const htmlMarkers = [
        {
            content: `<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(src/utils/marker-tools/image/cluster-marker-1.png);background-size:contain;"></div>`,
            size: new naver.maps.Size(40, 40),
            anchor: new naver.maps.Point(20, 20)
        },
        {
            content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(src/utils/marker-tools/image/cluster-marker-2.png);background-size:contain;"></div>',
            size: new naver.maps.Size(40, 40),
            anchor: new naver.maps.Point(20, 20)
        },
        {
            content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(src/utils/marker-tools/image/cluster-marker-3.png);background-size:contain;"></div>',
            size: new naver.maps.Size(40, 40),
            anchor: new naver.maps.Point(20, 20)
        },
        {
            content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(src/utils/marker-tools/image/cluster-marker-4.png);background-size:contain;"></div>',
            size: new naver.maps.Size(40, 40),
            anchor: new naver.maps.Point(20, 20)
        },
        {
            content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(src/utils/marker-tools/image/cluster-marker-5.png);background-size:contain;"></div>',
            size: new naver.maps.Size(40, 40),
            anchor: new naver.maps.Point(20, 20)
        }

    ]

    onMount(async () => {
        map = new naver.maps.Map('navermap', mapOptions)
        
        const res = await supplierApi.getList(0, 1000)
        suppliers = res.data

        const markers = suppliers.map(supplier => {
            const position = new naver.maps.LatLng(supplier.loc_y, supplier.loc_x)

            const infoWindowContent = [
            `<div class="m-3">`,
            `<a href="/supplier/${supplier.id}" class="link-offset-2 link-underline link-underline-opacity-0" target="_blank" rel="noopener noreferrer">`,
            `<h5 class="mb-0">${supplier.name}</h5>`,
            `<p class="link-dark">${supplier.address}</p>`,
            `</a></div>`,
            ].join('')

            const infoWindow = new naver.maps.InfoWindow({
                content: infoWindowContent,
                anchorSize: new naver.maps.Size(20, 20),
            })

            const marker = new naver.maps.Marker({position})
            naver.maps.Event.addListener(marker, "click", (event) => {
                if (infoWindow.getMap()) {
                    infoWindow.close()
                } else {
                    infoWindow.open(map, marker)
                }
            })
            return marker
        })

        const markerClustering = new MarkerClustering({
            minClusterSize: 2,
            maxZoom: 12,
            map: map,
            markers: markers,
	        disableClickZoom: false,
            icons: htmlMarkers,
            indexGenerator: [10, 100, 200, 500, 1000],
            stylingFunction:  (clusterMarker, count) => {
                clusterMarker.getElement().querySelector('div:first-child').innerText = count
            },
        })
    })

    $: {
        if (selectedSupplier) {
            const position = new naver.maps.LatLng(selectedSupplier.loc_y, selectedSupplier.loc_x)
            map.morph(position, 16)
        }
    }

</script>

<div class="container">
    <div class="" >
        <div class="row">
            <div class="col-md-8 px-1 mt-2">
                <div id="navermap" class="rounded" style="height: 70vh;"></div>
            </div>
            <div class="col-md-4 overflow-y-scroll px-1 mt-2" style="height: 70vh;">
                <div class="accordion accordion-flush" id="accordionFlushExample">
                    <div class="accordion-item">
                        <div class="accordion-header sticky-top border-bottom">
                            <button class="accordion-button" type="button" style="box-shadow:none;" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne">
                                <div class="fs-5 fw-semibold">수원지 목록</div>
                            </button>
                        </div>
                        <div id="flush-collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionFlushExample">
                            <div class="mt-1">
                                <MapSupplierList {suppliers} bind:selected={selectedSupplier}/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>